from backend.models.drawing_models import ParsedDrawingResult


def test_parsed_model_instantiation():
    payload = {
        'drawing_file': {'file_id': 'f1', 'filename': 'a.pdf', 'source_type': 'PDF'},
        'pages': [],
    }
    model = ParsedDrawingResult.model_validate(payload)
    assert model.drawing_file.file_id == 'f1'
