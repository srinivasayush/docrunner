import stripAnsi = require('strip-ansi')
import * as vscode from 'vscode'
import { runCommandWithProgressOutput } from '../utils/command'

const run = () => {
    runCommandWithProgressOutput('docrunner', ['run'], {
        location: vscode.ProgressLocation.Notification,
        title: 'Running docrunner run',
        cancellable: true,
    })
}

export const registerRunCommand = (context: vscode.ExtensionContext) => {
    const runCommand = vscode.commands.registerCommand('docrunner.run', run)
    context.subscriptions.push(runCommand)
}
