<script setup>
import { reactive } from 'vue';
import { useToast } from 'primevue/usetoast';
import Toast from 'primevue/toast';
import {InputText} from "primevue";
import {Message} from "primevue";
import {Button} from "primevue";
import {Form} from "@primevue/forms";

const toast = useToast();

const initialValues = reactive({
    username: ''
});

const resolver = ({ values }) => {
    const errors = {};

    if (!values.first_name) {
        errors.first_name = [{ message: 'First name is required.' }];
    }

	if (!values.last_name) {
        errors.last_name = [{ message: 'Last name is required.' }];
    }

    return {
        values, // Used to pass current form values to submit event.
        errors
    };
};

const onFormSubmit = ({ valid }) => {
    if (valid) {
        toast.add({
            severity: 'success',
            summary: 'Client successfully added',
            life: 4000
        });
    }
};
</script>

<template>
<div class="card flex justify-center">
	<Toast />

	<Form v-slot="$form" :initialValues :resolver @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-56">
		<div class="flex flex-row gap-1">
			<div>
				<label for="first_name">First name:</label>
			</div>
			<div class="flex flex-col gap-1">
				<InputText name="first_name" type="text" fluid />
				<Message v-if="$form.first_name?.invalid" severity="error" size="small" variant="simple">{{ $form.first_name.error?.message }}</Message>
			</div>
		</div>
		<div class="flex flex-row gap-1">
			<div>
				<label for="last_name">Last name:</label>
			</div>
			<div class="flex flex-col gap-1">
				<InputText name="last_name" type="text" fluid />
				<Message v-if="$form.last_name?.invalid" severity="error" size="small" variant="simple">{{ $form.last_name.error?.message }}</Message>
			</div>
		</div>
		<Button type="submit" severity="secondary" label="Add Client" />
	</Form>
</div>
</template>

<style scoped>

</style>