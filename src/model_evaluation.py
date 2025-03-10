import seaborn as sns
import matplotlib.pyplot as plt

def graph_model_history(history):
    """
    Takes as argument a model history: either the return of a KerasClassifier or the model.history of a Keras model.
    Plots model accuracy, validation accuracy, model loss, and validation loss training histories, if they are present in the history.history dictionary object:
    """
        
    import seaborn as sns
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1,2, figsize = (10,5))
    if 'acc' in history.history.keys():
        axes[0].plot(history.history['acc'], label = 'Train Accuracy')
    if 'val_acc' in history.history.keys():
        axes[0].plot(history.history['val_acc'], label = 'Validation Accuracy')
    axes[0].legend()
    if 'loss' in history.history.keys():
        axes[1].plot(history.history['loss'], label = 'Train Loss')
    if 'val_loss' in history.history.keys():
        axes[1].plot(history.history['val_loss'], label = 'Validation Loss')
    axes[1].legend()
    plt.show()


def plot_confusion_matrix(y_true,y_pred, save_path = None):
    """
    Uses sklearn.metrics.confusion_matrix to plot a seaborn heatmap with normalized labels for a 3x3 confusion matrix.  
    Inputs y_true and y_pred must each have 3 categories one column.
    take an optional argument: save_path = None or string-type filepath that defines the path to save the image at, if desired.  None means image will not be saved.
    """
    import seaborn as sns
    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt
    sns.set(context = 'notebook', style = 'whitegrid')

    
    sns.heatmap(confusion_matrix(y_true, y_pred, normalize = 'true'), 
            annot = True, 
            xticklabels = ['Pred Negative','Pred Neutral','Pred Positive'],
            yticklabels = ['Negative','Neutral','Positive'],
            cmap = ['#7890cd', '#748dcc', '#718acb', '#6d87ca', '#6a83c9', '#6680c8', 
                    '#637dc7', '#5f7ac6', '#5b76c5', '#5873c5', '#5470c4', '#516cc3', 
                    '#4d69c2', '#4966c1', '#4662c0', '#425fbf', '#3f5cbe', '#3e5aba', 
                    '#3c57b7', '#3b55b4', '#3a53b1', '#3851ae', '#374fab', '#354ca8', 
                    '#344aa5', '#3348a1', '#31469e', '#30449b', '#2f4298', '#2d4095', 
                    '#2c3e91', '#2b3c8e', '#2a3a8b', '#283888', '#273684', '#263481', 
                    '#25327e', '#23317b', '#222f77', '#212d74'])    
    if save_path:
        plt.savefig(save_path, dpi = 500, bbox_inches = 'tight', transparent = True)
    plt.xlabel = 'Predicted Sentiment'
    plt.ylabel = 'True Sentiment'
    plt.show()