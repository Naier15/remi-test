import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    products: [],
    basket: {},
    currency_rates: {},
    loading: false,
    host: 'http://172.20.10.11:8000',
    static: 'http://172.20.10.11:8000/static/main/img/',
    favicon: 'http://172.20.10.11:8000/static/main/img/favicon.jpg',
  },
  getters: {
    basket_count: () => {
      let storage = localStorage.getItem('my_basket') 
      if (storage === null) return
      storage = JSON.parse(storage)

      // console.log('basket_count - ', Object.values(storage))
      const sumQuantities = obj => Object.values(obj).reduce((acc, value) => acc + value['quantity'], 0);
      return storage === null ? 0 : sumQuantities(storage)
    }
  },
  mutations: {
    setLoading(state, value) {
      state.loading = value
    },

    addItem(state, product) {
      let storage = localStorage.getItem('my_basket') 
      storage = storage === null ? {} : JSON.parse(storage)

      const id = `${product.id}`
      const nextID = Object.keys(storage).length

      const index = Object.values(storage).findIndex( elem => elem.id == id )
      if (index !== -1) {
        storage[index].quantity += 1
      } else {
        let newItem = Object.assign({}, product, {'quantity': 1})
        storage[nextID] = newItem
      }
      localStorage.setItem('my_basket', JSON.stringify(storage, null, 4))
    },

  },
  actions: {
    async getProducts({state, commit}) {
      try {
        commit('setLoading', false)
        
        const response = await axios.get(`${state.host}/api/v1/products`)
        state.products = response.data

        commit('setLoading', true)
      } catch (err){
        console.log('[ERROR] function getProducts went wrong ', err)
      }
    },

    async get_currency_rates({state, commit}) {
      try {
        const response = await axios.get(`${state.host}/api/v1/currency`)
        state.currency_rates = response.data.data
      } catch (err) {
        console.log('[ERROR] function get_currency_rates went wrong ', err)
      }
    }

  },
  modules: {
  }
})
