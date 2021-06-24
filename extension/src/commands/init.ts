import * as vscode from 'vscode'
import { streamingRunCommand } from '../utils/command'

const init = () => {
    vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: 'Running docrunner init',
            cancellable: true,
        },
        async (_progress, token) => {
            token.onCancellationRequested((_event) => {
                vscode.window.showInformationMessage('Cancelled!')
            })

            const rootPath = vscode.workspace.workspaceFolders![0].uri.fsPath

            streamingRunCommand('docrunner', ['init'], {
                onStdout: (data) => {
                    console.log(data.toString())
                },
                onStdErr: (error) => {
                    console.log(error.toString())
                },
                spawnOptions: { cwd: rootPath },
            })
        }
    )
}

export const registerInitCommand = (context: vscode.ExtensionContext) => {
    const initCommand = vscode.commands.registerCommand('docrunner.init', init)
    context.subscriptions.push(initCommand)
}
