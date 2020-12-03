<script>
  import Container from "./Container.svelte";

  export let isOpen = false;
  export let stopId;
  export let lineId;
</script>

{#if isOpen}
  <Container>
    <h3 slot="title">Stop {stopId} - line {lineId}</h3>
    <div slot="body">TODO</div>
  </Container>
{/if}
