<script>
  import Container from "./Container.svelte";
  import ModeSwitcher from "./ModeSwitcher.svelte";

  export let isOpen;
  export let name = "";
  export let mode;
</script>

<style>
  .flex {
    display: flex;
    justify-content: space-around;
    height: 2rem;
  }

  input {
    width: 45%;
    height: 100%;
    border-radius: 16px;
    box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.1);
  }
</style>

{#if isOpen}
  <Container>
    <h3 slot="title">Filtrer les recherches</h3>
    <div class="flex" slot="body">
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
