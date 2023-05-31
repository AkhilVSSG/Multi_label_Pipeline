# Pipeline_Multi_label

This pipeline is used for Multi label classification which has 3 models namely FastXML , Catboost(with OneVsRest classification) , and Bert.

the directory roadmap is:

    code
        Bert
            convert_to_csv.py
            metrics_Bert.py
            train_Bert.py
        Catboost
            infer_Catboost.py
            metrics_Catboost.py
            train_Caboost.py
            vectorizer.py
        FastXML
            infer_FastXML.py
            metrics_FastXML.py
            train_FastXML.py
        fastxml(environment)
        data_preprocess.py
        pipeline.py
    data
        config.json
    static
        plots (saves the plots for the respective models)
        models (saves the trained model)

1. To start this pipeline first thing is to create a conda environment and install all the dependencies in the requirement.txt

2. then activate the environment and upload the raw data into the data directory.

3. after install all the dependencies in the requirements.txt

4. then we must run the data_preprocess.py you can edit the py file according to the columns you require and other requirements

5. you can see you will have train,test,val datasets

6. then we must run the pipeline file it will take data from the config file and start training

7. you can change the config file and train different models for the given data.

YOU ARE GOOD TO GO!!!

Personalization according to the user:
1. you can change the number of iterations and number of trees used by the FastXML model by going into the train_FastXML in FastXML in code directory and do the necessary changes

2. In the same way you can change the number of epochs in which a Bert model mu train which is available in train_Bert in Bert in code directory

3. you can even change the number of iterations and depth of a tree in Catboost by changing their values in the train_Caboost ni Catboost in code directory

4. all the models like Catboost and Bert are using their primary encoding methods i.e. CountVectorizer and auto tokenizer using roberta-base you can even change those and train your model. Those can be changed in vectorizer.py in Catboost and train_Bert.py in Bert respectively


