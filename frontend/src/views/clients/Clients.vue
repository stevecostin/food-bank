<script setup>
import { ref } from 'vue';
import { zodResolver } from '@primevue/forms/resolvers/zod';
import { useToast } from "primevue/usetoast";
import { z } from 'zod';
import { Form } from "@primevue/forms"
import {InputText, Message, Button, DatePicker} from "primevue";

const toast = useToast();

const initialValues = ref({
    firstName: '',
	lastName: '',
    email: '',
	dob: '',
	doorNumber: '',
	addressLine1: '',
	addressLine2: '',
	city: '',
	county: '',
	postCode: '',
	country: '',
	telephoneNumber: '',
});

const resolver = ref(zodResolver(
    z.object({
        firstName: z.string().min(1, { message: 'First name is required' }),
		lastName: z.string().min(1, { message: 'Last name is required' }),
		dob: z.preprocess((val) => {
            if (val === '' || val === null) {
                return null;
            }

            return new Date(val);
        }, z.union([z.date(), z.null().refine((val) => val !== null, { message: 'Date is required.' })]))
    })
));

const onFormSubmit = ({ valid }) => {
    if (valid) {
        toast.add({
			severity: 'success',
			summary: 'Form is submitted.',
			life: 4000,
		});
    }
};
</script>

<template>
<div class="card flex justify-center">
	<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" :validateOnMount="false" @submit="onFormSubmit" revalidateOn="submit" class="flex flex-col gap-4 w-full sm:w-56">
		<div class="flex flex-col gap-1">
			<InputText name="firstName" type="text" placeholder="First name" fluid />
			<Message v-if="$form.firstName?.invalid" severity="error" size="small" variant="simple">{{ $form.firstName.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="lastName" type="text" placeholder="Last name" fluid />
			<Message v-if="$form.lastName?.invalid" severity="error" size="small" variant="simple">{{ $form.lastName.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="email" type="text" placeholder="Email address" fluid />
			<Message v-if="$form.email?.invalid" severity="error" size="small" variant="simple">{{ $form.email.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="doorNumber" type="text" placeholder="Property number/name" fluid />
			<Message v-if="$form.doorNumber?.invalid" severity="error" size="small" variant="simple">{{ $form.doorNumber.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="addressLine1" type="text" placeholder="Address line 1" fluid />
			<Message v-if="$form.addressLine1?.invalid" severity="error" size="small" variant="simple">{{ $form.addressLine1.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="addressLine2" type="text" placeholder="Address line 2" fluid />
			<Message v-if="$form.addressLine2?.invalid" severity="error" size="small" variant="simple">{{ $form.addressLine2.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="city" type="text" placeholder="City" fluid />
			<Message v-if="$form.city?.invalid" severity="error" size="small" variant="simple">{{ $form.city.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="county" type="text" placeholder="County" fluid />
			<Message v-if="$form.county?.invalid" severity="error" size="small" variant="simple">{{ $form.county.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="postCode" type="text" placeholder="Postcode" fluid />
			<Message v-if="$form.postCode?.invalid" severity="error" size="small" variant="simple">{{ $form.postCode.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="country" type="text" placeholder="Country" fluid />
			<Message v-if="$form.country?.invalid" severity="error" size="small" variant="simple">{{ $form.country.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<InputText name="telephoneNumber" type="text" placeholder="Telephone number" fluid />
			<Message v-if="$form.telephoneNumber?.invalid" severity="error" size="small" variant="simple">{{ $form.telephoneNumber.error?.message }}</Message>
		</div>
		<div class="flex flex-col gap-1">
			<DatePicker name="dob" showIcon iconDisplay="input" placeholder="Date of birth" fluid />
			<Message v-if="$form.dob?.invalid" severity="error" size="small" variant="simple">{{ $form.dob.error?.message }}</Message>
		</div>
		<Button type="submit" severity="secondary" label="Submit" />
	</Form>
</div>
</template>