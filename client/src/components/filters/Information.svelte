<script>
  import Container from "./Container.svelte";

  export let isOpen = false;
  export let stopName;
  export let stopId;
  export let lineId;
</script>

{#if isOpen}
  <Container>
    <div slot="title">
      <h3>{stopName}</h3>
      <p>Stop {stopId} - line {lineId}</p>
    </div>
    <div slot="body">TODO</div>
  </Container>
{/if}
