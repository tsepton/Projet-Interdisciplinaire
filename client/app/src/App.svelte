<script>
  export let version;
  import Header from "./scrollparts/Header.svelte";
  import Main from "./scrollparts/Main.svelte";
</script>

<style>
  :global(:root) {
    --primary: #678ff5;
    --secondary: #475373;
    --ternary: #28407d;
    --quadrary: #192b59;
    --background: #f5f5f5;
    --foreground: #f5f5f5;
  }
</style>

<Header {version} />
<Main />
