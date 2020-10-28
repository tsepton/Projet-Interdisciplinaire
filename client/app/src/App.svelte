<script>
  export let version;
  import Header from "./scrollparts/Header.svelte";
  import Main from "./scrollparts/Main.svelte";
</script>

<Header {version} />
<Main />
