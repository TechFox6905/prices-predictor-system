from steps.data_ingestion_step import data_ingestion_step
from zenml import Model, pipeline, step


@pipeline(
    model=Model(
        # The name uniquely identifies this model
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""

    # Data Ingestion Step
    raw_data = data_ingestion_step(
        file_path=r"D:\VsCode\Machine Learning\prices-predictor-system\data\archive.zip"
    )


if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()
