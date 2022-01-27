from app import app
from flask import jsonify

@app.route('/collateral/{contract_name}/position/{id}')
def position_data(id):
    id = int(id)
    
    attributes = []
    _add_attribute(attributes, 'market',id)
    _add_attribute(attributes, 'side',id)
    _add_attribute(attributes, 'leverage',id)
    _add_attribute(attributes, 'debt',id)
    _add_attribute(attributes, 'cost',id)
    _add_attribute(attributes, 'maintenance',id)
    _add_attribute(attributes, 'collateral',id)
    _add_attribute(attributes, 'value',id)
    _add_attribute(attributes, 'pnl',id)
    _add_attribute(attributes, 'notional',id)
    _add_attribute(attributes, 'entry_price',id)
    _add_attribute(attributes, 'current_price',id)
    _add_attribute(attributes, 'liquidation_price',id)


    return jsonify({
    "description": "Positions issued by the <contract_name> collateral manager for Overlay V1 Core",
    "external_url": <external_url>,
    "image": <image_url>,
    "name": "<contract_name> Collateral Manager",
    "attributes": attributes 
    })


def _add_attribute(existing, attribute_name, token_id, display_type=None):
    trait = {
        'trait_type': attribute_name,
        'value': '#how to read from the contract'
    }
    if display_type:
        trait['display_type'] = display_type
    existing.append(trait)  

