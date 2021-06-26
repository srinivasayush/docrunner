import {
    ChildProcessWithoutNullStreams,
    spawn,
    SpawnOptionsWithoutStdio,
} from 'child_process'
import stripAnsi = require('strip-ansi')
import * as vscode from 'vscode'

interface StreamingRunCommandOptions {
    onStdout: (data: Buffer) => void
    onStdErr: (error: Buffer) => void
    onExit?: (exitCode: number | null) => void
    spawnOptions: SpawnOptionsWithoutStdio
}

export const runCommandWithOutputCallbacks = (
    entryPoint: string,
    commandArgs: string[],
    options: StreamingRunCommandOptions
): ChildProcessWithoutNullStreams => {
    const { onStdout, onStdErr, onExit, spawnOptions } = options

    const process = spawn(entryPoint, commandArgs, spawnOptions)

    process.stdout.on('data', onStdout)

    process.stderr.on('data', onStdErr)

    if (onExit) {
        process.on('exit', onExit)
    }
    return process
}

export const runCommandWithProgressOutput = (
    entryPoint: string,
    commandArgs: string[],
    options: vscode.ProgressOptions
) => {
    vscode.window.withProgress(options, async (_progress, token) => {
        token.onCancellationRequested((_event) => {
            vscode.window.showInformationMessage('Cancelled!')
        })

        const rootPath = vscode.workspace.workspaceFolders![0].uri.fsPath

        runCommandWithOutputCallbacks(entryPoint, commandArgs, {
            onStdout: async (data) => {
                const dataString = stripAnsi(data.toString())
                if (dataString.includes('Warning')) {
                    await vscode.window.showWarningMessage(dataString)
                }
                await vscode.window.showInformationMessage(dataString)
            },
            onStdErr: async (error) => {
                const errorString = stripAnsi(error.toString())
                await vscode.window.showErrorMessage(errorString)
            },
            spawnOptions: { cwd: rootPath },
        })
    })
}
