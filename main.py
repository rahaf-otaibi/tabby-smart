import streamlit as st

st.set_page_config(
    page_title="Tabby Smart",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Tabby Smart")
st.write("مساعد ذكي يساعدك على اتخاذ قرار شراء مناسب لميزانيتك")

st.divider()

st.header("💰 بياناتك المالية")

budget = st.number_input(
    "الميزانية الشهرية",
    min_value=0.0,
    value=3000.0
)

price = st.number_input(
    "سعر المنتج",
    min_value=0.0,
    value=1200.0
)

installments = st.number_input(
    "عدد الأقساط",
    min_value=1,
    value=4,
    step=1
)

commitments = st.number_input(
    "الالتزامات الشهرية",
    min_value=0.0,
    value=750.0
)

saving = st.number_input(
    "هدف الادخار الشهري",
    min_value=0.0,
    value=500.0
)

if st.button("📊 تحليل الشراء"):

    monthly_payment = price / installments

    available_money = budget - commitments - saving

    remaining_money = available_money - monthly_payment

    if available_money > 0:
        payment_percentage = (
            monthly_payment / available_money
        ) * 100
    else:
        payment_percentage = 100

    st.divider()

    st.header("📊 نتيجة التحليل")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "القسط الشهري",
            f"{monthly_payment:.2f} ريال"
        )

    with col2:
        st.metric(
            "المبلغ المتاح",
            f"{available_money:.2f} ريال"
        )

    with col3:
        st.metric(
            "المتبقي بعد القسط",
            f"{remaining_money:.2f} ريال"
        )

    st.write(
        f"📈 نسبة القسط من المبلغ المتاح: "
        f"{payment_percentage:.1f}%"
    )

    if remaining_money < 0:

        st.error(
            "🔴 الشراء قد يضغط على ميزانيتك"
        )

        st.info(
            "💡 نقترح البحث عن منتج بسعر أقل."
        )

    elif payment_percentage > 30:

        st.warning(
            "🟠 انتبه قبل إتمام الشراء"
        )

        st.info(
            "القسط يمثل نسبة مرتفعة من المبلغ المتاح."
        )

    else:

        st.success(
            "🟢 الشراء يبدو مناسباً لميزانيتك"
        )

        st.info(
            "لديك مبلغ متبقٍ بعد القسط والالتزامات والادخار."
        )

st.divider()

st.header("ماذا يقدم Tabby Smart؟")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("💰 تحليل الميزانية")
    st.write("معرفة المبلغ المتاح بعد الالتزامات والادخار.")

with col2:
    st.subheader("📅 حساب الأقساط")
    st.write("حساب قيمة القسط الشهري قبل إتمام عملية الشراء.")

with col3:
    st.subheader("🔔 تنبيهات ذكية")
    st.write("تنبيه المستخدم إذا كان الشراء قد يضغط على ميزانيته.")

with col4:
    st.subheader("💡 اقتراح بديل")
    st.write("اقتراح البحث عن منتج بسعر أقل عند الحاجة.")

st.caption("Tabby Smart - Prototype")