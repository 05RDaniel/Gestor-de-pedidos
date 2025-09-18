<template>
  <div v-if="visible" class="modal-overlay">
    <div class="modal">
      <h3>{{ title }}</h3>
      <p>{{ message }}</p>
      <div class="actions">
        <button class="cancel" @click="$emit('cancel')">
          {{ cancelText }}
        </button>
        <button 
          class="confirm"
          :style="{ backgroundColor: confirmColor }"
          @click="$emit('confirm')"
        >
          {{ confirmText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    visible: { type: Boolean, required: true },
    title: { type: String, default: "⚠️ Confirmar acción" },
    message: { type: String, default: "¿Seguro que deseas continuar?" },
    cancelText: { type: String, default: "Cancelar" },
    confirmText: { type: String, default: "Aceptar" },
    confirmColor: { type: String, default: "#42b983" } // verde por defecto
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal {
  background: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
  width: 300px;
}
.actions {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}
button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.cancel {
  background: #ccc;
}
.confirm {
  color: white;
}
</style>
