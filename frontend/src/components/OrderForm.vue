<template>
  <form class="order-form" @submit.prevent="saveOrder">
    <input v-model="order.customer" type="text" placeholder="Cliente" required />
    <input v-model="order.product" type="text" placeholder="Producto" required />
    <input v-model.number="order.quantity" type="number" placeholder="Cantidad" required />
    <button type="submit">{{ isEdit ? "💾 Guardar cambios" : "➕ Crear Pedido" }}</button>
  </form>
</template>

<script>
import axios from "axios"

export default {
  props: ["id"], // viene del router en modo edición
  data() {
    return {
      order: { customer: "", product: "", quantity: 1 },
      isEdit: false,
    }
  },
  async mounted() {
    if (this.id) {
      this.isEdit = true
      try {
        const res = await axios.get(`http://127.0.0.1:8000/api/orders/${this.id}/`)
        this.order = res.data
      } catch (err) {
        console.error("Error cargando pedido:", err)
      }
    }
  },
  methods: {
    async saveOrder() {
      try {
        if (this.isEdit) {
          await axios.put(`http://127.0.0.1:8000/api/orders/${this.id}/`, this.order)
        } else {
          await axios.post("http://127.0.0.1:8000/api/orders/", this.order)
        }
        this.$router.push("/") // volver a la lista
      } catch (err) {
        console.error("Error guardando pedido:", err)
      }
    },
  },
}
</script>

<style scoped>
.order-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 400px;
  margin: 0 auto;
}
.order-form input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 6px;
}
.order-form button {
  background: #42b983;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 6px;
  cursor: pointer;
}
.order-form button:hover {
  background: #2a8f6f;
}
</style>
