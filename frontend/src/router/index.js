import { createRouter, createWebHistory } from "vue-router"
import OrdersList from "../components/OrdersList.vue"
import OrderForm from "../components/OrderForm.vue"

const routes = [
  { path: "/", name: "Orders", component: OrdersList },
  { path: "/new", name: "NewOrder", component: OrderForm },
  { path: "/edit/:id", name: "EditOrder", component: OrderForm, props: true },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
