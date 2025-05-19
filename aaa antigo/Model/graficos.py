import pandas as pd
from pycaret.classification import load_model, predict_model
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE
from sklearn.metrics import roc_curve, auc, confusion_matrix

def load_all():
    model = load_model("model")
    iris = load_iris(as_frame=True)
    feature_names = iris.feature_names
    target_names = iris.target_names
    try:
        comparison_df = pd.read_csv("model_comparison.csv")
    except:
        comparison_df = None
    return model, iris, feature_names, target_names, comparison_df

def predict_species(model, feature_names, values):
    import pandas as pd
    input_data = pd.DataFrame([values], columns=feature_names)
    prediction = predict_model(model, data=input_data)
    pred_class = int(prediction["prediction_label"][0])
    return pred_class

def get_tsne_3d(iris):
    tsne = TSNE(n_components=3, random_state=42)
    iris_tsne = tsne.fit_transform(iris.data)
    return iris_tsne

def get_roc_data(model, iris):
    y_true = iris.target
    y_score = model.predict_proba(iris.data)[:, 1]
    fpr, tpr, _ = roc_curve(y_true, y_score, pos_label=1)
    roc_auc = auc(fpr, tpr)
    return fpr, tpr, roc_auc

def get_confusion_matrix(model, iris):
    y_true = iris.target
    y_pred = model.predict(iris.data)
    cm = confusion_matrix(y_true, y_pred)
    return cm