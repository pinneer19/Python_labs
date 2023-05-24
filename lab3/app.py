from serializer.serializers.serializer_factory import SerializerFactory
import typer

app = typer.Typer()


@app.command()
def serializer(source_file: str, result_file: str, source_format: str, result_format: str):
    source_serializer = SerializerFactory.get_serializer(source_format)
    result_serializer = SerializerFactory.get_serializer(result_format)
    with open(source_file, 'r') as rf, open(result_file, 'w') as wt:
        temp_res = source_serializer.load(rf)
        print(temp_res)
        result_serializer.dump(temp_res, wt)


if __name__ == "__main__":
    app()
