import streamlit as st
from Model.graficos import load_all, predict_species, get_tsne_3d, get_roc_data, get_confusion_matrix
from View.gerargraficos import show_predict_page, show_comparison_page, show_3d_page, show_roc_page, show_confusion_page


model, iris, feature_names, target_names, comparison_df = load_all()

st.sidebar.title("🧪 Iris Classifier")
page = st.sidebar.radio("Choose page", ["🧬 Predict", "📊 Compare Models", "Grafico 3D", "Grafico ROC", "Grafico Confusão"])

if page == "🧬 Predict":
    show_predict_page(feature_names, target_names, lambda values: predict_species(model, feature_names, values))

elif page == "📊 Compare Models":
    show_comparison_page(comparison_df)

elif page == "Grafico 3D":
    iris_tsne = get_tsne_3d(iris)
    show_3d_page(comparison_df, iris_tsne, iris.target)

elif page == "Grafico ROC":
    fpr, tpr, roc_auc = get_roc_data(model, iris)
    show_roc_page(comparison_df, fpr, tpr, roc_auc)

elif page == "Grafico Confusão":
    cm = get_confusion_matrix(model, iris)
    show_confusion_page(comparison_df, cm, target_names)