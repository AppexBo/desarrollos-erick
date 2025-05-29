/** @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    setup() {
        super.setup(...arguments);
        debugger
		this.changePos(this.pos);
	}, 

    changePos(pos){
        const observer = new MutationObserver(() => {
            this.hide_info_button_products_pdv();
            this.hide_in_information_finanzas();
            this.hide_in_information_ordenars();
        });
        
        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    },

    hide_info_button_products_pdv(){
        // Seleccionar todos los elementos con la clase "product-information-tag"
        const info_buttons = document.querySelectorAll(".product-information-tag");
        // Ocultar los elementos encontrados
        info_buttons.forEach(info_button => {
            // Verificar tiene el campo esta visible
            const have_styles = info_button.hasAttribute('style');
            if (!have_styles) {
                info_button.setAttribute('style', 'display: none !important;')
            }
        });
    },

    hide_in_information_finanzas(){
        const section_financials = document.querySelectorAll(".section-financials.mt-3.mb-4.pb-4.border-bottom.text-start");
        section_financials.forEach(section_financial => {
            const have_styles = section_financial.hasAttribute('style');
            if (!have_styles) {
                section_financial.setAttribute('style', 'display: none !important;')
            }
        });
    },

    hide_in_information_ordenars(){
        const section_orders = document.querySelectorAll(".section-order.mt-3.mb-4.pb-4.border-bottom.text-start");
        section_orders.forEach(section_order => {
            const have_styles = section_order.hasAttribute('style');
            if (!have_styles) {
                section_order.setAttribute('style', 'display: none !important;')
            }
        });
    },

});