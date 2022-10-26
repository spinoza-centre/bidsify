from pathlib import Path
import logging
import yaml
import subprocess


def main() -> None:
    # logging the running of the conversions across projects
    log_dir = Path.home() / 'logs' / 'bidsify'
    log_dir.mkdir(exist_ok=True)
    logging.basicConfig(filename=log_dir / 'bidsify.log',
                        encoding='utf-8',
                        level=logging.DEBUG)

    config_path = Path(__file__).parent / 'site.yml'
    with open(config_path) as config:
        cfg = yaml.safe_load(config)
    submit_script_templatefile = Path(__file__).parent / 'SoGE_submit.sh'
    submit_text = submit_script_templatefile.read_text()

    local_project_path = Path(cfg.get('project_path'))
    project_folders = [pf for pf in local_project_path.glob('*') if pf.isdir()]
    project_PIs, project_names = zip([pf.name.split('_')
                                      for pf in project_folders])

    for i, project_name in enumerate(project_names):
        logging.info(f'Processing {project_name}')
        project_path = project_folders[i]
        for subfolder in ['bids', 'parrec', 'mriqc', 'scripts']:
            subf_path = project_path / subfolder
            subf_path.mkdir(exist_ok=True)

        project_yaml_file = project_path / 'bidsify.yml'
        # only attempt conversion on projects with yaml file
        if not project_yaml_file.exists():
            logging.warning(f'No bidsify.yml file found in {project_path}')
            continue

        pr_sm_txt = submit_text.replace('PROJECT_PATH', project_path)
        pr_sm_txt = pr_sm_txt.replace('PROJECT', project_name)
        pr_sm_file = project_path / 'script' / '{project_name }_SoGE_submit.sh'
        pr_sm_file.write_text(pr_sm_txt)

        # submit the actual shell script we've just edited
        subprocess.run(["qsub", "-V", pr_sm_file], capture_output=True)


if __name__ == '__main__':
    main()
