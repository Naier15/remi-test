<template>
    <Header 
        :basket_count="basket_count"/>
    <Main @update_basket_count="update_basket_count" />
    <Footer />
</template>

<script>
import Main from '@/components/Main.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
    name: 'Menu',
    components: {
        Header, Main, Footer
    },
    data() {
        return {
            basket_count: null,
        }
    },
    methods: {
        get_basket_count() {
            this.basket_count = this.$store.getters.basket_count
        },
        update_basket_count() {
            this.get_basket_count()
        }
    }, 
    mounted() {
        this.get_basket_count()
    }
}
</script>

<style scoped>

</style>