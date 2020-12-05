<script>
  import Container from "./Container.svelte";
  import { stopsByLine } from "../../lib/api.js";
  import Destination from "./Destination.svelte";

  export let isOpen = false;
  export let stopName;
  export let stopId;
  export let lineId;
</script>

<style>
  hr {
    border: transparent;
    border-top: 0.01rem dashed grey;
    margin-bottom: 1.2rem;
  }
</style>

{#if isOpen}
  <Container>
    <div slot="title">
      <h3>{stopName}</h3>
    </div>
    <div slot="body">
      <p>Stop n°{stopId} - ligne {lineId}</p>
      <hr />
      {#await stopsByLine([lineId])}
        Loading...
      {:then { lines }}
        {#each lines as line, index}
          <Destination {line} />
          {#if index < 1}
            <hr />
          {/if}
        {/each}
      {/await}
    </div>
  </Container>
{/if}
