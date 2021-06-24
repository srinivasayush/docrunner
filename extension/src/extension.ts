import * as vscode from 'vscode'
import { registerInitCommand } from './commands/init'

export function activate(context: vscode.ExtensionContext) {
    registerInitCommand(context)
}

// this method is called when your extension is deactivated
export function deactivate() {}
