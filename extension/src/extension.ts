import * as vscode from 'vscode'
import { registerInitCommand } from './commands/init'
import { registerRunCommand } from './commands/run'

export function activate(context: vscode.ExtensionContext) {
    registerInitCommand(context)
    registerRunCommand(context)
}

// this method is called when your extension is deactivated
export function deactivate() {}
