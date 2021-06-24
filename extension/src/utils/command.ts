import {
    ChildProcessWithoutNullStreams,
    spawn,
    SpawnOptionsWithoutStdio,
} from 'child_process'

interface StreamingRunCommandOptions {
    onStdout: (data: Buffer) => void
    onStdErr: (error: Buffer) => void
    onExit?: (exitCode: number | null) => void
    spawnOptions: SpawnOptionsWithoutStdio
}

export const streamingRunCommand = (
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
