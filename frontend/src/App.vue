<template>
  <div class="app-container">
    <h1>📦 Gestor de Pedidos</h1>
    <router-view /> <!-- aquí se mostrarán las vistas -->
  </div>
</template>

<script>
export default { name: "App" }
</script>

<style>
.app-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  font-family: Arial, sans-serif;
  text-align: center;
}
</style>
