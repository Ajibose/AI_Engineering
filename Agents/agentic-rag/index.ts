import { runMemoryAgent, runAISupportAgent } from './agents';


async function main() {
  const query = 'what is agent parallelization and how do i edit my profile';
  const chunks = await runMemoryAgent(query);

  const completion = await runAISupportAgent({
    chunks,
    query,
  });

  console.log('completion', completion);
}

main();
