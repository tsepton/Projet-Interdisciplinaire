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
      <p>Délais prévus pour l'arret séléctionné</p>
    </div>
    <div slot="body">
      <p>Tous les arrêts</p>
    </div>
  </Container>
{/if}
