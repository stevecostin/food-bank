<script setup>
import { Button, InputText, Password, useToast } from "primevue";
import { ref } from 'vue';
import { useAuthStore } from "@/stores/auth.js";
import { useRouter, useRoute } from 'vue-router'
import { Form } from '@primevue/forms';
import api from "@/components/api.js";

const router = useRouter();
const route = useRoute();
const toast = useToast();

const email = ref(null);
const password = ref(null);

const authStore = useAuthStore();

const onFormSubmit = async ({ valid }) => {
	const formData = {
		email: email.value,
		password: password.value,
	};

	try {
		let response = await api.post('/accounts/login', formData);

		const token = response.data;

		if (token.success) {
			authStore.login();
		}

		await router.push(route.query.to || '/');

		toast.add({ severity: 'success', summary: 'Form is submitted.', life: 3000 });
	} catch (e) {
		console.error(e);
	}
};
</script>

<template>
<Form v-slot="$form" @submit="onFormSubmit" class="flex flex-col gap-3 w-full sm:w-64">
	<div class="card flex">
        <div class="flex flex-col gap-1">
			<label for="email">Email</label>
			<InputText type="text" v-model="email" id="email" variant="filled" />
		</div>
	</div>
	<div class="card flex">
        <div class="flex flex-col gap-1">
			<label for="password">Password</label>
			<Password v-model="password" :feedback="false" id="password" variant="filled" toggleMask />
		</div>
	</div>
	<div class="card flex">
        <div class="flex flex-col gap-1">
			<Button type="submit" severity="secondary" label="Login" />
		</div>
	</div>
</Form>
</template>

<style scoped>

</style>