'use strict'

const core = require("@actions/core");
const github = require("@actions/github");
const { promise: fs } = require('fs');

const main = async () => {
  const file = core.getInput("file");

  let content = await fs.readFile(file, 'utf8');

  console.log(content);

  let changelog = content.split("\n\n##")[0];

  core.setOutput("changelog", changelog);
}

main().catch(err => core.setFailed(err.message));
