from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)


def test_health():
    resp = client.get('/health')
    data = resp.json()
    assert resp.status_code == 200
    assert data['ok'] is True
    assert data['stage'] == 'P0'


def test_rules_load():
    resp = client.get('/rules')
    data = resp.json()
    assert data['ok'] is True
    assert isinstance(data['rules'], list)
    assert any(r['rule_id'] == 'QTY-CONC-001' for r in data['rules'])


def test_rule_not_found():
    resp = client.get('/rules/not-exist')
    data = resp.json()
    assert resp.status_code == 404
    assert data['ok'] is False


def test_quantity_explain_success():
    payload = {'rule_id': 'QTY-CONC-001', 'inputs': {'length': 2, 'width': 3, 'height': 4, 'unit': 'm3'}}
    resp = client.post('/quantity/explain', json=payload)
    data = resp.json()
    assert data['ok'] is True
    assert data['quantity_item']['quantity'] == 24


def test_review_basic_success():
    payload = {'rule_id': 'REV-REBAR-001', 'elements': [{'element_id': 'e-1', 'confidence': 0.3}]}
    resp = client.post('/review/basic', json=payload)
    data = resp.json()
    assert data['ok'] is True
    assert len(data['issues']) == 1


def test_mock_parse_stable_json():
    resp = client.post('/drawings/parse/mock')
    data = resp.json()
    assert data['ok'] is True
    result = data['result']
    assert 'drawing_file' in result
    assert result['pages'][0]['elements'][0]['confidence'] >= 0
    assert 'source_ref' in result['pages'][0]['elements'][0]


def test_normalize_success():
    payload = client.post('/drawings/parse/mock').json()['result']
    resp = client.post('/drawings/normalize', json=payload)
    data = resp.json()
    assert data['ok'] is True
    assert data['result']['drawing_file']['source_type'] == 'PDF'


def test_normalize_missing_fields_controlled_error():
    resp = client.post('/drawings/normalize', json={'pages': []})
    data = resp.json()
    assert resp.status_code == 400
    assert data['ok'] is False
    assert 'details' in data


def test_schema_response():
    resp = client.get('/drawings/schema')
    data = resp.json()
    assert data['ok'] is True
    assert 'confidence' in data['core_fields']
