<script setup>
import { RouterView } from 'vue-router'
import { useRouter } from 'vue-router';
import { ref } from "vue";
import Menubar from 'primevue/menubar';
import { Avatar } from "primevue";
import 'primeicons/primeicons.css'

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
        items: [
            {
                label: 'Shopping List',
				command: () => {
					router.push('/shopping');
				}
            },
            {
                label: 'Stock Management',
				command: () => {
					router.push('/stock');
				}
            },
        ]
    },
]);
</script>

<template>
<div>
	<Menubar :model="items">
	    <template #start>
			LOGO
		</template>
		<template #item="{ item, props, hasSubmenu, root }">
			<a class="flex items-center" v-bind="props.action">
				<span>{{ item.label }}</span>
				<i v-if="hasSubmenu" :class="['pi pi-angle-down ml-auto']"></i>
			</a>
		</template>
		<template #end>
			<div class="flex items-center gap-2">
				<Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
			</div>
		</template>
	</Menubar>
</div>
<div id="main">
	<RouterView />
</div>
</template>

<style scoped>

</style>
