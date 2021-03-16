<template>
  <div id="app">
    <Toolbar></Toolbar>
    <!-- Routes get rendered here -->
    <router-view></router-view>
  </div>
</template>

<script>
import Toolbar from './components/Toolbar'

export default {
    components: {
      Toolbar,
    },
}
</script>
