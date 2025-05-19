import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def show_predict_page(feature_names, target_names, predict_callback):
    st.title("🌸 Iris Species Prediction")
    sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.1)
    sepal_width = st.slider("Sepal width (cm)", 2.0, 4.5, 3.5)
    petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 1.4)
    petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 0.2)
    if st.button("Predict"):
        pred_class = predict_callback([sepal_length, sepal_width, petal_length, petal_width])
        st.success(f"Predicted species: **{target_names[pred_class]}**")

def show_comparison_page(comparison_df):
    st.title("📊 Model Comparison (Accuracy)")
    if comparison_df is not None:
        st.dataframe(comparison_df)
        st.bar_chart(comparison_df.set_index("Model")["Accuracy"])
    else:
        st.warning("No comparison data available.")

def show_3d_page(comparison_df, iris_tsne, iris_target):
    st.title("Grafico 3D")
    if comparison_df is not None:
        st.dataframe(comparison_df)
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(
            iris_tsne[:, 0], iris_tsne[:, 1], iris_tsne[:, 2],
            c=iris_target, cmap='viridis', s=50
        )
        ax.set_title("t-SNE 3D Visualization")
        ax.set_xlabel("Dimensão 1")
        ax.set_ylabel("Dimensão 2")
        ax.set_zlabel("Dimensão 3")
        legend = ax.legend(*scatter.legend_elements(), title="Espécies", loc="upper right")
        ax.add_artist(legend)
        st.pyplot(fig)
    else:
        st.warning("No comparison data available.")

def show_roc_page(comparison_df, fpr, tpr, roc_auc):
    st.title("Grafico ROC")
    if comparison_df is not None:
        st.dataframe(comparison_df)
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, color="blue", label=f"ROC curve (area = {roc_auc:.2f})")
        ax.plot([0, 1], [0, 1], color="gray", linestyle="--")
        ax.set_title("Curva ROC")
        ax.set_xlabel("Taxa de Falsos Positivos (FPR)")
        ax.set_ylabel("Taxa de Verdadeiros Positivos (TPR)")
        ax.legend(loc="lower right")
        st.pyplot(fig)
    else:
        st.warning("No comparison data available.")

def show_confusion_page(comparison_df, cm, target_names):
    st.title("Grafico Confusão")
    if comparison_df is not None:
        st.dataframe(comparison_df)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=target_names, yticklabels=target_names, ax=ax)
        ax.set_title("Matriz de Confusão")
        ax.set_xlabel("Predito")
        ax.set_ylabel("Verdadeiro")
        st.pyplot(fig)
    else:
        st.warning("No comparison data available.")