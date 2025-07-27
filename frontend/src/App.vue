<script setup>
import { RouterView } from 'vue-router'
import { ref } from "vue";
import Menubar from 'primevue/menubar';
import { useRouter } from 'vue-router';

const router = useRouter();

const items = ref([
    {
        label: 'Dashboard',
		command: () => {
			router.push('/');
		}
    },
    {
        label: 'People',
        items: [
            {
                label: 'Clients',
				command: () => {
					router.push('/clients');
				}
            },
            {
                label: 'Staff',
				command: () => {
					router.push('/staff');
				}
            },
        ]
    },
    {
        label: 'Stock',
		command: () => {

		}
    },
]);
</script>

<template>
<div>
	<Menubar :model="items" />
</div>
<div id="main">
	<RouterView />
</div>
</template>

<style scoped>

</style>
