from bert_serving.server.helper import get_args_parser
from bert_serving.server import BertServer
args = get_args_parser().parse_args(['-model_dir', '/app/bert-models/current',
                                     '-port', '5555',
                                     '-port_out', '5556',
                                     '-max_seq_len', '1024',
                                     '-mask_cls_sep',
                                     '-max_batch_size', '16',
                                     '-cpu'])
server = BertServer(args)
server.start()