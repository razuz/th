# Using sigma-cli and community rules with Elasticsearch

### Clone Sigma rules and install sigma-cli

```shell
git clone https://github.com/SigmaHQ/sigma.git
cd sigma
python3 -m venv venv
source venv/bin/activate
pip install sigma-cli
```

### Converting community rules to Elasticsearch

- List which target SIEM solutions can sigma-cli convert to

    ```shell
    sigma plugin list
    ```
- Install the elasticsearch converter

    ```shell
    sigma plugin install elasticsearch
    ```
- Check which formats of Elasticsearch queries are supported (think Lucene or EQL aka SIEM rules)

    ```shell
    sigma list formats elasticsearch
    ```

- List pipelines aka what field names schema to use

    ```shell
    sigma list pipelines
    ```

- Convert any given Sigma community rule to an Elasticsearch Lucene query where the field names conform to elastic common schema

    ```shell
    sigma convert -t elasticsearch -f default -p ecs_windows rules/windows/process_creation/proc_creation_win_powershell_base64_encoded_cmd.yml
    ```

