import yaml
from hcl import dumps
def yaml_to_hcl(yaml_data):
    hcl_data = {}
    for key, value in yaml_data.items():
        if isinstance(value, dict):
            hcl_data[key] = yaml_to_hcl(value)
        else:
            hcl_data[key] = value
    return hcl_data
def main():
    with open('input.yaml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    
    hcl_data = yaml_to_hcl(yaml_data)
    with open('terraform.tfvars', 'w') as hcl_file:
        hcl_file.write(dumps(hcl_data))
if name == "__main__":
    main()
