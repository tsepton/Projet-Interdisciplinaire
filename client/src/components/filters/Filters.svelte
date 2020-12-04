<script>
  import Container from "./Container.svelte";
  import ModeSwitcher from "./ModeSwitcher.svelte";

  export let isOpen;
  export let name = "";
  export let mode;
</script>

<style>
  input {
    width: 100%;
  }
</style>

{#if isOpen}
  <Container>
    <h3 slot="title">Filtrer les recherches</h3>
    <div slot="body">
      <input
        id="input"
        type="text"
        name="name"
        placeholder="Chercher une station..."
        bind:value={name} />
      <ModeSwitcher bind:mode />
    </div>
  </Container>
{/if}
