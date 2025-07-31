<script setup>
import {RouterView} from 'vue-router'
import {ref} from "vue";
import Menubar from 'primevue/menubar';
import {Avatar} from "primevue";

const items = ref([
    {
        label: 'People',
        icon: 'pi pi-users',
        items: [
            {
                label: 'Clients',
				route: '/clients'
            },
        ]
    },
    {
        label: 'Stock',
        icon: 'pi pi-shopping-cart',
        items: [
            {
                label: 'Shopping List',
            },
            {
                label: 'Stock Management',
            },
        ]
    },
    {
        label: 'Reporting',
        icon: 'pi pi-chart-line',
        items: [
            {
                label: 'Report 1',
            },
        ]
    },
    {
        label: 'Admin',
        icon: 'pi pi-lock',
        items: [
            {
                label: 'Staff',
            },
			{
				separator: true,
			},
            {
                label: 'Site Settings',
            },
        ]
    },
]);
</script>

<template>
<div>
    <div class="card">
		<Menubar :model="items">
			<template #start>
				LOGO
			</template>
			<template #item="{ item, props, hasSubmenu, root }">
				<router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
                    <a :href="href" v-bind="props.action" @click="navigate">
                        <span :class="item.icon" />
                        <span>{{ item.label }}</span>
                    </a>
                </router-link>
				<a v-else :href="item.url" :target="item.target" v-bind="props.action">
                    <span :class="item.icon" />
                    <span>{{ item.label }}</span>
                    <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down" />
                </a>
			</template>
			<template #end>
				<div class="flex items-center gap-2">
					<Avatar label="SC" shape="circle" />
				</div>
			</template>
		</Menubar>
	</div>
</div>
<div id="main">
	<RouterView />
</div>
</template>

<style scoped>

</style>
