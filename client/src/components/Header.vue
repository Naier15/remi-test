<template>
<header>
  <nav id="navbar-example2" class="navbar fixed-top px-3 mb-3 header">
    <div class="container">
      <img class="favicon" :src=$store.state.favicon alt="icon" >
      <div v-if="$store.state.currency_rates" class="currency">
        <span>Доллар: {{$store.state.currency_rates.dollar}}</span>
        <span>Евро: {{$store.state.currency_rates.euro}}</span>
        <span class="updated_time"><i>Обновлено: {{$store.state.currency_rates.minutes}} минут {{$store.state.currency_rates.seconds}} секунд назад</i></span>
      </div>
      <div class="six"><h1><span>Магазин у дивана</span></h1></div>
      <div class="header-right">
        <ul class="nav nav-pills nav-fill gap-2 p-1 small bg-white border rounded-5 shadow-sm" id="pillNav2" role="tablist">
          <li class="nav-item" role="presentation">
            <a @click="goToMenu" class="nav-link rounded-5" :class="[menu_active]" id="home-tab2" aria-selected="true" tabindex="1">Меню</a>
          </li>
          <li class="nav-item" role="presentation">
            <a @click="goToBasket" class="nav-link rounded-5" :class="[basket_active]" id="profile-tab2" aria-selected="false" tabindex="2">Корзина</a>
          </li>
          <li v-if="basket_count" class="circle">
            <span class="basket-count">{{basket_count}}</span>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</header>
</template>

<script>
import store from '@/store'

export default {
    name: 'Header',
    props: {
      basket_count: {
        type: Number,
        required: false
      },
    },
    data() {
      return {
        dollar: null,
        euro: null,
        minutes: null,
        seconds: null,
        menu_active: "",
        basket_active: "",
      }
    },
    methods: {
      goToBasket(){
        this.$router.push({name: 'Basket'})
      },
      goToMenu() {
        this.$router.push({name: 'Menu'})
      },
    },
    mounted() {
      if (this.$router.currentRoute.value.path === "/vue") {
        this.menu_active = 'active'
      } else if (this.$router.currentRoute.value.path === "/vue/basket") {
        this.basket_active = 'active'
      }
   
      store.dispatch('get_currency_rates')
    } 
      
}
</script>

<style scoped>
.header {
    background-color: rgb(224, 247, 248);
    border-bottom-right-radius: 30px 30px;
    border-bottom-left-radius: 30px 30px;
}

.container {
    max-width: 1180px;
}

.favicon {
    object-fit: cover;
    object-position: 70% 50%;
    width: 80px;
    height: 80px;
    border-radius: 50px;
}

.currency {
    display: flex;
    flex-direction: column;
    color: #267dff;
}

.updated_time {
    font-size: 10px;
}

.six {
    padding: 20px 20px;
    text-align: center;
}
.six h1 {
    font-weight: 600;
    font-family: 'Merriweather', serif;
    position: relative;
    display: inline-block;
    margin: 0;
    line-height: 1;
    color: #267dff;
    font-size: 22px;
    padding: .4em 1em .55em;
}
.six h1:before,
.six h1:after {
    content: ""; 
    position: absolute;
    width: 60%;
    height: .1em;
    background: #8fbafa; 
}
.six h1:before {
    left: 0;
    top: 0;
}
.six h1:after {
    right: 0;
    bottom: 0;
}
.six h1 span:before,
.six h1 span:after {
    content: ""; 
    position: absolute;
    width: .65em;
    height: .65em;
    border: .13em solid #8fbafa;
    border-radius: 50%;
    box-sizing: border-box;
}
.six h1 span:before {
    top: -.55em;
    left: -.325em;
}
.six h1 span:after {
    bottom: -.55em;
    right: -.325em;
}
@media (max-width: 600px) {
    .six h1 {font-size: 2em;}
}
@media (max-width: 450px) {
    .six h1 {font-size: 1.5em;}
}

.basket-count {
    padding: 8px;
    color: #0d6efd;
    font: 16px Arial, sans-serif;
}

.circle {
    border: 1px solid #0d6efd;
    background: rgb(224, 247, 248);
    border-radius: 50%;
    height: 1.5rem;
    align-self: center;
    position: relative;
    left: -10px;
}
</style>