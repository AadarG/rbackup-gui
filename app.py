from flask import Flask, render_template, request
import toml
from .config import dict_to_config

app = Flask(__name__)

# Going to this route will display the configuration read from a TOML file
# If the method is POST, then the new config file is parsed as a Config object.
@app.route('/', methods=['GET', 'POST'])
def config_editor():
    if request.method == 'POST':
        config_toml = request.form['config']
        config_dict = toml.loads(config_toml)
        # Process the config dictionary as needed
        config = dict_to_config(config_dict)
        # Render the template with the updated config
        print(config)
        print(config.targets)
    else:
        # Load the initial config from the file
        with open('/home/pratik/.config/rbackup/config.toml', 'r') as f:
            config_toml = f.read()
    print(config_toml)
    return render_template('config.html', config=config_toml)

if __name__ == '__main__':
    app.run()
