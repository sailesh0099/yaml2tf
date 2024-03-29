import yaml
def convert_yaml_to_tfvars(yaml_file, tfvars_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    with open(tfvars_file, 'w') as f:
        for key, value in data.items():
            f.write(f"{key} = \"{value}\"\n")
if name == "__main__":
    convert_yaml_to_tfvars("values.yaml", "values.tfvars")
