from .base_options import BaseOptions


class TestOptions(BaseOptions):
    def initialize(self, parser):
        BaseOptions.initialize(self, parser)
        parser.add_argument('--results_dir', type=str, default='../results/', help='saves results here.')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        parser.add_argument('--num_test', type=int, default=50, help='how many test images to run')
        parser.add_argument('--n_samples', type=int, default=5, help='#samples')
        parser.add_argument('--no_encode', action='store_true', help='do not produce encoded image')
        parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio for the results')

        self.isTrain = False
        parser.set_defaults(batch_size=1)
        parser.set_defaults(num_threads=1)
        return parser
