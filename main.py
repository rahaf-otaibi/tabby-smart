from nicegui import ui


# =========================
# تحليل عملية الشراء
# =========================

def analyze_purchase():
    budget = float(budget_input.value or 0)
    price = float(price_input.value or 0)
    installments = int(installments_input.value or 0)
    commitments = float(commitments_input.value or 0)
    saving = float(saving_input.value or 0)

    if budget <= 0 or price <= 0 or installments <= 0:
        result_area.clear()

        with result_area:
            ui.label(
                "⚠️ يرجى إدخال جميع البيانات بشكل صحيح"
            ).classes(
                "text-red-600 text-lg font-bold"
            )

        return

    # حساب القسط الشهري
    monthly_payment = price / installments

    # المبلغ المتاح بعد الالتزامات والادخار
    available_money = budget - commitments - saving

    # المبلغ المتبقي بعد دفع القسط
    remaining_money = available_money - monthly_payment

    # نسبة القسط من المبلغ المتاح
    if available_money > 0:
        payment_percentage = (
            monthly_payment / available_money
        ) * 100
    else:
        payment_percentage = 100

    # =========================
    # عرض النتيجة
    # =========================

    result_area.clear()

    with result_area:

        ui.label(
            "📊 نتيجة التحليل"
        ).classes(
            "text-2xl font-bold"
        )

        ui.separator()

        ui.label(
            f"💳 القسط الشهري: "
            f"{monthly_payment:.2f} ريال"
        ).classes(
            "text-lg"
        )

        ui.label(
            f"💰 المبلغ المتاح: "
            f"{available_money:.2f} ريال"
        ).classes(
            "text-lg"
        )

        ui.label(
            f"💵 المتبقي بعد القسط: "
            f"{remaining_money:.2f} ريال"
        ).classes(
            "text-lg"
        )

        ui.label(
            f"📈 نسبة القسط: "
            f"{payment_percentage:.1f}%"
        ).classes(
            "text-lg"
        )

        ui.separator()

        # =========================
        # حالة الشراء
        # =========================

        if remaining_money < 0:

            ui.label(
                "🔴 الشراء قد يضغط على ميزانيتك"
            ).classes(
                "text-xl font-bold text-red-600"
            )

            ui.label(
                "نقترح البحث عن منتج بسعر أقل."
            ).classes(
                "text-md"
            )

        elif payment_percentage > 30:

            ui.label(
                "🟠 انتبه قبل إتمام الشراء"
            ).classes(
                "text-xl font-bold text-orange-500"
            )

            ui.label(
                "القسط يمثل نسبة مرتفعة من المبلغ المتاح."
            ).classes(
                "text-md"
            )

        else:

            ui.label(
                "🟢 الشراء يبدو مناسباً لميزانيتك"
            ).classes(
                "text-xl font-bold text-green-600"
            )

            ui.label(
                "لديك مبلغ متبقٍ بعد القسط والالتزامات والادخار."
            ).classes(
                "text-md"
            )


# =========================
# مسح البيانات
# =========================

def clear_data():

    budget_input.value = None
    price_input.value = None
    installments_input.value = None
    commitments_input.value = None
    saving_input.value = None

    result_area.clear()

    with result_area:

        ui.label(
            'أدخل بياناتك ثم اضغط "تحليل الشراء"'
        ).classes(
            "text-gray-500 text-lg"
        )


# =========================
# عنوان الصفحة
# =========================

ui.page_title("Tabby Smart")


# =========================
# الصفحة الرئيسية
# =========================

with ui.column().classes(
    "w-full max-w-6xl mx-auto p-6"
):

    # العنوان

    ui.label(
        "💡 Tabby Smart"
    ).classes(
        "text-4xl font-bold text-center w-full"
    )

    ui.label(
        "مساعد ذكي يساعدك على اتخاذ قرار شراء مناسب لميزانيتك"
    ).classes(
        "text-lg text-gray-500 text-center w-full mb-8"
    )


    # =========================
    # القسم الرئيسي
    # =========================

    with ui.row().classes(
        "w-full items-start gap-6"
    ):

        # =========================
        # بيانات المستخدم
        # =========================

        with ui.card().classes(
            "w-full md:w-5/12 p-6"
        ):

            ui.label(
                "بياناتك المالية"
            ).classes(
                "text-2xl font-bold"
            )

            ui.label(
                "أدخل معلوماتك حتى نحلل عملية الشراء."
            ).classes(
                "text-gray-500 mb-5"
            )

            budget_input = ui.number(
                label="الميزانية الشهرية",
                placeholder="مثال: 3000"
            ).classes(
                "w-full"
            )

            price_input = ui.number(
                label="سعر المنتج",
                placeholder="مثال: 1200"
            ).classes(
                "w-full"
            )

            installments_input = ui.number(
                label="عدد الأقساط",
                placeholder="مثال: 4",
                min=1
            ).classes(
                "w-full"
            )

            commitments_input = ui.number(
                label="الالتزامات الشهرية",
                placeholder="مثال: 750"
            ).classes(
                "w-full"
            )

            saving_input = ui.number(
                label="هدف الادخار الشهري",
                placeholder="مثال: 500"
            ).classes(
                "w-full"
            )

            # زر التحليل

            ui.button(
                "تحليل الشراء",
                on_click=analyze_purchase,
                icon="analytics"
            ).classes(
                "w-full mt-4"
            )

            # زر المسح

            ui.button(
                "مسح البيانات",
                on_click=clear_data,
                icon="delete"
            ).props(
                "outline"
            ).classes(
                "w-full mt-2"
            )


        # =========================
        # نتيجة التحليل
        # =========================

        with ui.card().classes(
            "w-full md:w-6/12 p-6"
        ):

            result_area = ui.column().classes(
                "w-full"
            )

            with result_area:

                ui.label(
                    "📊 نتيجة التحليل"
                ).classes(
                    "text-2xl font-bold"
                )

                ui.label(
                    'أدخل بياناتك ثم اضغط "تحليل الشراء"'
                ).classes(
                    "text-gray-500 mt-3"
                )


    # =========================
    # المميزات
    # =========================

    ui.label(
        "ماذا يقدم Tabby Smart؟"
    ).classes(
        "text-2xl font-bold text-center w-full mt-10"
    )


    with ui.row().classes(
        "w-full justify-center gap-4"
    ):

        # الميزة الأولى

        with ui.card().classes(
            "w-full md:w-1/5 p-4"
        ):

            ui.label("💰").classes(
                "text-3xl"
            )

            ui.label(
                "تحليل الميزانية"
            ).classes(
                "text-xl font-bold"
            )

            ui.label(
                "معرفة المبلغ المتاح بعد الالتزامات والادخار."
            )


        # الميزة الثانية

        with ui.card().classes(
            "w-full md:w-1/5 p-4"
        ):

            ui.label("📅").classes(
                "text-3xl"
            )

            ui.label(
                "حساب الأقساط"
            ).classes(
                "text-xl font-bold"
            )

            ui.label(
                "حساب قيمة القسط الشهري قبل إتمام عملية الشراء."
            )


        # الميزة الثالثة

        with ui.card().classes(
            "w-full md:w-1/5 p-4"
        ):

            ui.label("🔔").classes(
                "text-3xl"
            )

            ui.label(
                "تنبيهات ذكية"
            ).classes(
                "text-xl font-bold"
            )

            ui.label(
                "تنبيه المستخدم إذا كان الشراء قد يضغط على ميزانيته."
            )


        # الميزة الرابعة

        with ui.card().classes(
            "w-full md:w-1/5 p-4"
        ):

            ui.label("💡").classes(
                "text-3xl"
            )

            ui.label(
                "اقتراح بديل"
            ).classes(
                "text-xl font-bold"
            )

            ui.label(
                "اقتراح البحث عن منتج بسعر أقل عند الحاجة."
            )


    # =========================
    # أسفل الصفحة
    # =========================

    ui.separator().classes(
        "mt-10"
    )

    ui.label(
        "Tabby Smart - Prototype"
    ).classes(
        "text-center text-gray-500 w-full"
    )


# =========================
# تشغيل التطبيق
# =========================

ui.run(
    title="Tabby Smart",
    port=8080
)