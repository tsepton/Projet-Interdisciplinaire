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
  }

  @media (max-width: 900px) {
    .flex {
      height: max-content;
      flex-direction: column;
      padding: 10px;
    }
    .spacer {
      display: none;
    }
  }
  @media (min-width: 900px) {
    .flex {
      height: 2rem;
      flex-direction: row;
    }
    .spacer {
      width: 1rem;
    }
  }

  input {
    width: 100%;
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
      <div class="spacer" />
      <ModeSwitcher bind:mode />
    </div>
  </Container>
{/if}
