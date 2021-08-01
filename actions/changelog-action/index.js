'use strict'

const core = require('@actions/core');
const github = require('@actions/github');
const { promises: fs } = require('fs');

const main = async () => {
  const file = core.getInput('file');

  let content = await fs.readFile(file, 'utf8');

  content = content.split("\n\n##")[0];

  core.setOutput('data', content);
}

main().catch(err => core.setFailed(err.message));
