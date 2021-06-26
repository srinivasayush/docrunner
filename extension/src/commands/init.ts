import * as vscode from 'vscode'
import { runCommandWithProgressOutput } from '../utils/command'

const init = () => {
    runCommandWithProgressOutput('docrunner', ['init'], {
        location: vscode.ProgressLocation.Notification,
        title: 'Running docrunner run',
        cancellable: true,
    })
}

export const registerInitCommand = (context: vscode.ExtensionContext) => {
    const initCommand = vscode.commands.registerCommand('docrunner.init', init)
    context.subscriptions.push(initCommand)
}
