'use strict'

const core = require("@actions/core");
const github = require("@actions/github");
const { promise: fs } = require('fs');

const main = async () => {
  const file = core.getInput("file");

  console.log(file);
  //let content = await fs.readFile(file, 'utf8');

  //let changelog = content.split("\n\n##")[0];

  core.setOutput('changelog', "test");
}

main().catch(err => core.setFailed(err.message));
