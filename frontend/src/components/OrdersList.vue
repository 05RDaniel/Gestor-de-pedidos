<template>
  <div>
    <button class="add-btn" @click="$router.push('/new')">➕ Nuevo Pedido</button>

    <table class="orders-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Cliente</th>
          <th>Producto</th>
          <th>Cantidad</th>
          <th>Fecha</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td>{{ order.id }}</td>
          <td>{{ order.customer }}</td>
          <td>{{ order.product }}</td>
          <td>{{ order.quantity }}</td>
          <td>{{ new Date(order.created_at).toLocaleString() }}</td>
          <td>
            <button @click="$router.push('/edit/' + order.id)">✏️ Editar</button>
            <button @click="askDelete(order)">🗑️ Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal reutilizable -->
    <ConfirmDialog 
      :visible="showConfirm"
      title="❌ Eliminar Pedido"
      message="¿Seguro que quieres eliminar este pedido?"
      cancelText="Cancelar"
      confirmText="Eliminar"
      confirmColor="#e74c3c"
      @cancel="showConfirm = false"
      @confirm="confirmDelete"
    />
  </div>
</template>

<script>
import axios from "axios"
import ConfirmDialog from "./ConfirmDialog.vue"

export default {
  components: { ConfirmDialog },
  data() {
    return { 
      orders: [],
      showConfirm: false,
      orderToDelete: null
    }
  },
  mounted() {
    this.loadOrders()
  },
  methods: {
    async loadOrders() {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/orders/")
        this.orders = res.data
      } catch (err) {
        console.error("Error al cargar pedidos:", err)
      }
    },
    askDelete(order) {
      this.orderToDelete = order
      this.showConfirm = true
    },
    async confirmDelete() {
      if (!this.orderToDelete) return
      try {
        await axios.delete(`http://127.0.0.1:8000/api/orders/${this.orderToDelete.id}/`)
        this.loadOrders()
      } catch (err) {
        console.error("Error eliminando pedido:", err)
      }
      this.showConfirm = false
      this.orderToDelete = null
    }
  }
}
</script>



<style scoped>
.add-btn {
  margin-bottom: 1rem;
  background: #42b983;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 6px;
  cursor: pointer;
}
.add-btn:hover {
  background: #2a8f6f;
}
.orders-table {
  width: 100%;
  border-collapse: collapse;
}
.orders-table th,
.orders-table td {
  padding: 0.75rem;
  border: 1px solid #ddd;
}
.orders-table th {
  background: #f4f4f4;
}
.orders-table button {
  margin: 0 5px;
  padding: 0.3rem 0.6rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.orders-table button:first-child {
  background: #f39c12;
  color: white;
}
.orders-table button:last-child {
  background: #e74c3c;
  color: white;
}
</style>
